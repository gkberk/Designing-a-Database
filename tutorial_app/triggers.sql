CREATE TRIGGER DrugCascade
AFTER DELETE ON drug
FOR EACH ROW
BEGIN
DELETE FROM interaction
	WHERE drug.drugID = interaction.drug2ID;
DELETE FROM causes
	WHERE drug.drugID = causes.drugID;
DELETE FROM partof
	WHERE drug.drugID = partof.drugID;
END



CREATE TRIGGER ProteinCascade
AFTER DELETE ON protein
FOR EACH ROW
BEGIN
DELETE FROM proteinreaction
	WHERE protein.proteinID = proteinreaction.proteinID;
END




