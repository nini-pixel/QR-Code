# Written by Nicia Ebosiri
# Helper function program

def convert_date (date_str):
    '''
    Returns a dictionary with "Day", "Month" and "Year" as keys and strings as
    values from an input 
    Parameters:
        date_str (a string): a date string in the format "dd/mm/yyyy"
    
    Result:
        date_dict (a dict): a dictionary with "Day", "Month" and "Year" as
        keys and strings as values
    
    Examples:
     >>> convert_date("09/01/2024")
     {'Day': '09', 'Month': '01', 'Year': '2024'}
     >>> convert_date("09/2024")
     Traceback (most recent call last):
     ValueError: Input format incorrect!
     >>> convert_date("0/0/2024")
     Traceback (most recent call last):
     ValueError: Input format incorrect!
    
    '''
    
    if len(date_str) != 10 or date_str[2] != '/' or date_str[5] != '/':
        raise ValueError ('Input format incorrect!')
    
    else:
        date_str = date_str.split('/')
        if len(date_str[0]) != 2 or len(date_str[1]) != 2 or \
           len(date_str[2]) != 4 or len(date_str) != 3:
            raise ValueError ('Input format incorrect!')
        else:
            date_dict = {'Day': date_str[0], 'Month': date_str[1], \
                         'Year': date_str[2]}
            return date_dict


def get_data (file):
    '''
    Returns a nested list of integers from an input string
    
    Parameters:
        file_path (a string): location of the file
    
    Result:
        nested_list (list): nested list of integers representing data in the file
    
    Examples:
    >>> get_data("small_data.txt")
    [[0, 1], [1, 0]]
    >>> get_data("small_data_error1.txt")
    Traceback (most recent call last):
    ValueError: File should contain only 0s and 1s!
    >>> get_data("small_data_error2.txt")
    Traceback (most recent call last):
    ValueError: File should contain only 0s and 1s!
    
    '''
    fobj = open(file,'r')
    file_path = fobj.read()
    
    # Split to keep the numbers only
    file_list = file_path.split('\n')
    
    nested_list = []
    
    for lists in file_list:
        if lists:
            nested_list1 = []
            for character in lists:
                # Constraint testing         
                if character != '0' and character != '1':
                    raise ValueError ('File should contain only 0s and 1s!')
                    
                else: 
                    nested_list1.append(int(character))
            
            # Add to nested list for each row
            nested_list.append(nested_list1)
    
    fobj.close()    
    return nested_list
