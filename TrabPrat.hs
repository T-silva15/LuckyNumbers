module TrabPrat where
import System.Exit (exitSuccess)
import System.Process (system)
import Distribution.Backpack.PreModuleShape (PreModuleShape(PreModuleShape))
import System.IO (readFile, IOMode(WriteMode), withFile, hPutStr)

import Data.Maybe (listToMaybe, mapMaybe)
import Text.Read (readMaybe)
import Data.List (groupBy, sortBy)
import Data.Function (on)
import Control.Monad (forM_)
import Data.Map (Map)
import qualified Data.Map as Map


-- type synoyms
type StudentID = String
type SubjectID = Int
type SubjectMap = Map SubjectID [StudentID]

-- Main function (executes menu)
main :: IO ()
main = menu

-- Menu function
menu :: IO()
menu =  do
    system "cls"                                                       -- clears screen       
    putStrLn "/ / / / / / MENU / / / / / /"                            -- prompt to present available options to user
    putStrLn "(1)   Criar ficheiro com escalonamento dos exames"
    putStrLn "(2)   Apresentar incompatibilidades"
    putStrLn " "
    putStrLn "(0)   Encerrar o programa"
    putStrLn "Selecione uma opçao:"
    input <- getLine                                                 -- asks user for input
    case input of                                                    -- case clause with input to call function(s) needed
        "1" -> tar1
--        "2" -> tar2
--        "0" -> exitSuccess
        _ -> doesntExist input


-- Function that takes in a file path and returns a list with the words in that file


readFileWords :: FilePath -> IO [String]
readFileWords path = do
  contents <- readFile path
  return (words contents)                                               -- returns wordlist of that file


tar1:: IO ()                                                           -- function that creates file with the exam scheduling
tar1 = do
  putStrLn "Introduza o número de dias disponíveis: "
  days <- readLn
  putStrLn "Introduza o número de salas disponíveis: "
  rooms <- readLn
  contents <- readFile "inscricoes.txt"
  let inscr = words contents
      highNumber = findHighestNumber inscr
  case highNumber of
    Just number -> if number > days * rooms
                     then putStrLn "Nao é possível realizar os exames com essas condiçoes"
                     else do
                      putStrLn "É possível!"
                      ucsGrupo <- createSubjectMap "inscricoes.txt"
                      writeSubjectGroups ucsGrupo "divisãoUcs.txt"
    Nothing -> putStrLn "Nao foi possível obter o número mais alto."


findHighestNumber :: [String] -> Maybe Int         -- finds the highest number in list (used to determine how many subjects there are)
findHighestNumber strings = case numbers of
  [] -> Nothing
  _ -> Just (maximum numbers)
  where
    numbers = mapMaybe readMaybe strings

parseLine :: String -> (StudentID, SubjectID)      -- takes a line from the input file and parses it into a tuple (StudentID, SubjectID)
parseLine line =
  case words line of
    [student, subject] -> (student, read subject)
    _ -> error "Invalid line format"

createSubjectMap :: FilePath -> IO SubjectMap      -- This function reads the contents of the input file and constructs a SubjectMap ()
createSubjectMap filePath = do
  contents <- readFile filePath
  let linesList = lines contents
  let subjectList = map parseLine linesList
  let subjectMap = foldr insertIntoMap Map.empty subjectList
  return subjectMap

insertIntoMap :: (StudentID, SubjectID) -> SubjectMap -> SubjectMap       -- inserts the student ID into the list of students enrolled in the corresponding subject ID
insertIntoMap (student, subject) = Map.insertWith (++) subject [student]

writeSubjectGroups :: SubjectMap -> FilePath -> IO ()       -- writes the subject groups to the specified file (divisãoUcs.txt)
writeSubjectGroups subjectMap filePath = do
  withFile filePath WriteMode $ \handle ->
    let formattedGroups = Map.toList subjectMap
        formattedLines = map formatLine formattedGroups
        groupsContent = unlines formattedLines
    in hPutStr handle groupsContent

formatLine :: (SubjectID, [StudentID]) -> String      -- takes a subject ID and a list of students and formats them as a string
formatLine (subject, students) =
  show subject ++ " " ++ unwords students

-- tar2 :: IO()
-- tar2 = do
--  putStrLn "Introduza o número de dias disponíveis: "
--  days <- readLn
--  putStrLn "Introduza o número de salas disponíveis: "
--  rooms <- readLn


-- Error handling
doesntExist :: String -> IO ()
doesntExist opt =
  putStrLn $ "A opção " ++ opt ++ " não existe"
