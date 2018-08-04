import sys
global str
import helper


class topCostDrug():

    def __init__(self):
        self.dictCost = {}
        self.dictPrescriber = {}

    # The function to process each input line
    def processLine(self, line):
        fields = line.split(',')
        ID = fields[0]
        lastName = fields[1]
        firstName = fields[2]
        drugName = fields[3]
        drugCost = fields[4]

        # Using the helper to check the format of the input line
        if helper.validate_line(ID, lastName, firstName, drugName, drugCost):
            # Record the drug cost and the prescriber's full name into two separate dictionaries
            # For the prescriber's dictionary, a set is used so only the unique individuals would be recorded for each drug name
            drugCost = int(float(drugCost))
            fullName = lastName.upper() + ':' + firstName.upper()
            if drugName not in self.dictCost:
                self.dictCost[drugName] = drugCost
                self.dictPrescriber[drugName] = {fullName}
            else:
                self.dictCost[drugName] += drugCost
                self.dictPrescriber[drugName] |= {fullName}

    # The function to open the input file, process it, and write the result into the output file
    def pharmacyCounting(self, inputFile, outputFile):
        f_input = open(inputFile, 'r')
        # Streaming each line from input file
        for line in f_input.readlines():
            self.processLine(line)
        f_input.close()

        f_output = open(outputFile, 'w+')  
        f_output.write('drug_name,num_prescriber,total_cost\n')
        # The drugs are sorted in descending order based on the total drug cost and if there is a tie, drug name.
        # The '-item[1]' is to make sure the descending order of the total drug cost
        for k, v in sorted(self.dictCost.items(), key = lambda item:(-item[1], item[0])):
            f_output.write(str(k) + ',' + str(len(self.dictPrescriber[k])) + ',' + str(int(v)) + '\n')
        f_output.close



def main():
    # Read in all the argv for the .py file
    input_file = sys.argv[1:][0]
    output_file = sys.argv[1:][1]
    ct = topCostDrug()
    ct.pharmacyCounting(input_file, output_file)

if __name__ == "__main__":
    main()
