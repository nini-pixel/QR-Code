import copy
import helper

class TxtData:
    '''
    Stores the data from a text
    
    Instance attributes:
        data (a list): a nested list of integer representing the data
        rows (an integer): an integer indicating the number of rows in data
        cols (an integer): an integer indicating the number of columns in data
        
    '''
    
    def __init__ (self, data):
        '''
        Takes in a nested list that it deep copies using the deep copy
        function
    
        Parameters:
            data (a list): a 2D nested list with at least one row and
            column respectively
    
        Examples:
        >>> my_list_simple= [[1,2,3],[4,5,6]]
        >>> my_txt_simple = TxtData(my_list_simple)
        >>> my_txt_simple.rows
        2
        >>> my_txt_simple.cols
        3
        >>> my_list = get_data("small_data.txt")
        >>> my_txt = TxtData(my_list)
        >>> my_txt.rows
        2
        >>> my_txt.cols
        2
        >>> my_list_simple= [[1,6],[1,5]]
        >>> my_txt_simple = TxtData(my_list_simple)
        >>> my_txt_simple.rows
        2
        >>> my_txt_simple.cols
        2
        
        '''
        self.data = copy.deepcopy (data)
        self.rows = len(self.data)
        self.cols = len(self.data[0])
    
    def __str__ (self):
        '''
        Returns a string of format "This TxtData object has ROWS rows and
        COLS columns."
        
        Results:
            string (a string): a string of specified format
            
        Examples:
        >>> my_list_simple = [[1,2,3],[4,5,6]]
        >>> my_txt_simple = TxtData(my_list_simple)
        >>> print(my_list_simple)
        This TxtData object has 2 rows and 3 columns.
        >>> my_list_simple = [[1,2],[4,6]]
        >>> my_txt_simple = TxtData(my_list_simple)
        >>> print(my_list_simple)
        This TxtData object has 2 rows and 2 columns.
        >>> my_list_simple = [[1,4],[5,4]]
        >>> my_txt_simple = TxtData(my_list_simple)
        >>> print(my_list_simple)
        This TxtData object has 2 rows and 2 columns.

        '''
        string = 'This TxtData object has ' + str(self.rows) + ' rows and ' \
                 + str(self.cols) + ' columns.'
        
        return string

    def get_pixels (self):
        '''
        Returns an integer of the total number of pixels in data by
        multiplying the number of rows with the number of columns
        
        Parameters:
            None
            
        Results:
            num_pixels (an integer): the total number of pixels in data
            
        Example:
        >>> my_list_simple = [[1,2,3],[4,5,6]]
        >>> my_txt_simple = TxtData(my_list_simple)
        >>> my_txt_simple.get_pixels()
        6        
        >>> my_list_simple = [[1,2],[4,6]]
        >>> my_txt_simple = TxtData(my_list_simple)
        >>> my_txt_simple.get_pixels()
        4 
        >>> my_list_simple = [[1,2,3,3],[4,5,6,3]]
        >>> my_txt_simple = TxtData(my_list_simple)
        >>> my_txt_simple.get_pixels()
        8
        
        '''
        num_pixels = self.cols * self.rows
        return num_pixels
        
    def get_data_at (self, row, col):
        '''
        Returns an integer indicating the value in data at a position
        indicated through the row and col parameters. Raises a ValueError
        if the position is out of bound
        
        Parameters:
            row (an integer): position in terms of row
            col (an integer): position in terms of column
        
        Results:
            output_int (an integer): value in data at the position specified
            in parameters
            
        Examples:
        >>> my_list_simple =[[1,2,3],[4,5,6]]
        >>> my_txt_simple =TxtData(my_list_simple)
        >>> my_txt_simple.get_data_at(0,0)
        1
        >>> my_list_simple =[[8,2],[13,9]]
        >>> my_txt_simple =TxtData(my_list_simple)
        >>> my_txt_simple.get_data_at(0,0)
        8
        >>> my_txt_simple.get_data_at(5,0)
        Traceback(most recentcall last):
        ValueError:Index outof bound!
        
        '''
        if row >= self.rows or col >= self.cols:
            raise ValueError ('Index out of bound!')
        
        else:
            output_int = self.data[row][col]
            return output_int

    def pretty_save (self, file_name):
        '''
        Converts data from a file to a prettier form to be scannable as a QR
        code
        
        Parameters:
            file_name (a string): a file name
            
        Results:
            None
            
        Examples:
        >>> my_list = get_data("qrcode_binary.txt")
        >>> my_txt = TxtData(my_list)
        >>> my_txt.pretty_save("qrcode_pretty.txt")
        >>> my_list = get_data("small_data.txt")
        >>> my_txt = TxtData(my_list)
        >>> my_txt.pretty_save("pretty_small_data.txt")
        >>> my_list = get_data("data.txt")
        >>> my_txt = TxtData(my_list)
        >>> my_txt.pretty_save("pretty_data.txt")
        
        '''
        output_file = open(file_name, 'w')
        
        for line in self.data:
            for data_value in line:
                if data_value == 1:
                    output_file.write('\u2588' + '\u2588')
                elif data_value == 0:
                    output_file.write('  ')
            output_file.write('\n')
        
        output_file.close()

    def equals (self, another_data):
        '''
        Returns whether or not (True or False) two TxtData objects are equal
        by evaluating if their data attributes are identical
        
        Parameters:
            another_data (a list): another list and a TxtData object
            
        Results:
            True or False (a boolean): a boolean value indicating if two
            TxtData objects are equal
        
        Examples:
        >>> my_list_simple = [[1,2,3],[4,5,6]]
        >>> my_txt_simple_1 =TxtData(my_list_simple)
        >>> my_txt_simple_2 =TxtData(my_list_simple)
        >>> my_txt_simple_1.equals(my_txt_simple_2)
        True 
        >>> lists = [[1,2],[3,4]]
        >>> list1 = TxtData(lists)
        >>> list2 = TxtData(lists)
        True
        >>> list1 = TxtData([[7,4],[3,2]])
        >>> list2 = TxtData([[5,1],[6,21])
        >>> list1.equals(list2)
        False
        
        '''        
        for index in range (len(self.data)):
            for value_index in range (len(self.data[index])):
                if self.data[index] != another_data.data[index]:
                    return False
            
        return True
    
    def approximately_equals (self, another_data, precision):
        '''
        Returns whether or not two TxtData objects are approximately equal
        after comparing 
        
        Parameters:
            another_data (a list): a TxtData object
            precision (a float): a non-negative float
            
        Results:
            True or False (a boolean): indicates if the two TxtData objects
            are approximately equal
            
        Examples:
        >>> my_list_simple_1 = [[1,2,3],[4,5,6]]
        >>> my_list_simple_2 = [[1,2,3],[7,8,9]]
        >>> my_txt_simple_1 = TxtData(my_list_simple_1)
        >>> my_txt_simple_2 = TxtData(my_list_simple_2)
        >>> my_txt_simple_1.equals(my_txt_simple_2)
        False
        >>> my_txt_simple_1.approximately_equals(my_txt_simple_2, 0.5)
        True
        >>> my_list_simple_1 = [[1,2,3],[4,5,6]]
        >>> my_list_simple_2 = [[1,2,3],[7,8,9]]
        >>> my_txt_simple_1 = TxtData(my_list_simple_1)
        >>> my_txt_simple_2 = TxtData(my_list_simple_2)
        >>> my_txt_simple_1.equals(my_txt_simple_2)
        False
        >>> my_txt_simple_1.approximately_equals(my_txt_simple_2, 0.1
        False
        >>> my_list_simple_1 = [[1,2,3],[4,5,6]]
        >>> my_list_simple_2 = [[1,2,3],[7,8,9]]
        >>> my_txt_simple_1 = TxtData(my_list_simple_1)
        >>> my_txt_simple_2 = TxtData(my_list_simple_2)
        >>> my_txt_simple_1.equals(my_txt_simple_2)
        False
        >>> my_txt_simple_1.approximately_equals(my_txt_simple_2, 1)
        True
         
        '''
        counter_different_values = 0
        
        for index in range (self.rows):
            for value_index in range (self.cols):
                if self.get_data_at(index, value_index) !=\
                another_data.get_data_at(index, value_index):
                    counter_different_values += 1
        
        total_pixels = another_data.get_pixels()
        inconsistent_rate = counter_different_values / total_pixels
        
        return not (inconsistent_rate > precision)
