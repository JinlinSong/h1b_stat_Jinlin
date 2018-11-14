'''
Python Version: Python 3.6.1 :: Anaconda custom (x86_64)

Author: Jinlin Song
Datetime: 11/14/2018 08:00:00 AM
'''

### Import the module needed
import sys

class H1B_CSV:
    '''
    Define class H1B_CSV.
    Given the file path, it loads csv data into class H1B_CSV;
    Method is_valid() returns True if we load the data succesfully.
    Method data_header() returns the data_header;
    Method data_set() returns the data only;
    '''
    def __init__(self, data_file, sep = ';'):
        self.value = True
        self.data_input = []
        try:
            with open(data_file,'r') as f:
                for row in f:
                    self.data_input.append(row.strip('\n').split(sep))
        except:
            print('Error: Not able to load csv data from the given input file, please check the path!')
            self.value = False

    ### Data load validation method
    def is_valid(self):
        return self.value
    
    ### Data header method 
    def data_header(self):
        return self.data_input[0] if self.value else None
    
    ### Data method
    def data_set(self):
        return self.data_input[1:] if self.value else None

def certified_data(data_set, data_header, column_name_list, certified_value):
    '''
    Given data, data header, column_name_list [state, occupation, status], returns certified extracted data.
    ''' 
    column_index_list = []
    for column_name in column_name_list:
        try:
            ### Get the index of related columns
            column_index_list.append(data_header.index(column_name))
        except:
            print('Error:', column_name, 'is not in the CSV column names, please specify the correct column name!\nCSV column names are:')
            for column_name in data_header:
                print(column_name)
            return False
    
    ### Extract related columns
    data_extracted = [[e[i].strip('"') for i in column_index_list] for e in data_set]
    
    ### Return certified records
    data_certified = [e[:2] for e in data_extracted if e[2] == certified_value]
    
    return data_certified

class H1B_stat:
    '''
    Given certified data, return top 10 occupations and states.
    '''
    def __init__(self, data_certified):
        self.data_certified = data_certified
        self.total_records = len(data_certified)

    ### Get results of top 10 occupations and top 10 states
    def data_stat(self):
        occupation_stat_dict = {}
        state_stat_dict = {}
        for record in self.data_certified:
            ### Occupations
            if record[1] in occupation_stat_dict:
                occupation_stat_dict[record[1]] += 1
            else:
                occupation_stat_dict[record[1]] = 1

            ### States
            if record[0] in state_stat_dict:
                state_stat_dict[record[0]] += 1
            else:
                state_stat_dict[record[0]] = 1

        ### Sort occupation stats, state stats
        occupation_stat_set = sorted(occupation_stat_dict.items(), key = lambda kv: (-kv[1], kv[0]), reverse = False)[:10]
        state_stat_set = sorted(state_stat_dict.items(), key = lambda kv: (-kv[1], kv[0]), reverse = False)[:10]

        ### Add percentage
        occupation_stat_set = [[e[0], e[1], float(round(100*e[1]/self.total_records, 1))] for e in occupation_stat_set]            
        state_stat_set = [[e[0], e[1], float(round(100*e[1]/self.total_records, 1))] for e in state_stat_set]

        return [occupation_stat_set, state_stat_set]

def write_data(dataset, path, data_type):
    '''
    Write data to the given file.
    '''
    file_header = "NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE"
    with open(path, 'w') as f:
        if data_type == 'TOP_OCCUPATIONS':
            file_header = "TOP_OCCUPATIONS;" + file_header
        elif data_type == 'TOP_STATES':
            file_header = "TOP_STATES;" + file_header
        else:
            print("Error: Invalid data_type, please specify data_type as 'TOP_OCCUPATIONS' or 'TOP_STATES'.")
            return False
        
        ### Write header to the output file
        f.write(file_header + '\n')
        
        ### Convert integer to string
        dataset_output = [[e[0], str(e[1]), str(e[2]) + '%'] for e in dataset]
        
        ### Write data to the output file
        for item in dataset_output:
            f.write(";".join(item) + '\n')
    return True

def main(input_path, top_10_occupations_path, top_10_states_path):
    ### Specify state_column_name, occupation_column_name, status_column_name and certified_value
    state_column_name = 'WORKSITE_STATE' 
    occupation_column_name = 'SOC_NAME' 
    status_column_name = 'CASE_STATUS'
    certified_value = 'CERTIFIED'
    column_name_list = [state_column_name, occupation_column_name, status_column_name]

    ### Get H1B CSV data in the csv file
    H1B_CSV_var = H1B_CSV(data_file = input_path, sep = ';')
    if not H1B_CSV_var.is_valid:
        sys.exit()

    data_header = H1B_CSV_var.data_header()
    data_set = H1B_CSV_var.data_set()

    data_certified = certified_data(data_set, data_header, column_name_list, certified_value)
    if not data_certified:
        sys.exit()

    ### Process certified H1B data to get top_10_occupations and top_10_states
    H1B_stat_var = H1B_stat(data_certified)
    occupation_stat, state_stat = H1B_stat_var.data_stat()
    
    ### Write data to top_10_occupations, and top_10_states file
    write_data(occupation_stat, top_10_occupations_path, data_type = 'TOP_OCCUPATIONS')
    write_data(state_stat, top_10_states_path, data_type = 'TOP_STATES')
    return True

if __name__ == '__main__':
    ### Get input path and output path from sys.
    if len(sys.argv) != 4:
        print('Please specify Four parameters: h1b_counting.py, input path, top_10_occupations path and top_10_states path!')
    else:
        input_path_var, top_10_occupations_path_var, top_10_states_path_var = sys.argv[1:]
        main(input_path_var, top_10_occupations_path_var, top_10_states_path_var)

