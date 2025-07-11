import helper
import txtdata

class QRCode:
    '''
    Defines a class QR code that has four instance attributes
    
    Instance attributes:
        last_update_date (a dictionary): a dictionary with "Day", "Month",
        and "Year" as keys and strings representing the last update date of
        the QR code as values
        owner (a string): a string representing the owner of the QR code
        data (a TxtData object): a TxtData object representing the QR code
        error_correction (a float): indicated the error correction capability
        of the QR code (the max value of the damage rate before the QR code
        is unreadable)
        
    '''
    
    def __init__ (self, file_path, last_update_date = '00/00/0000', \
                  owner = 'Default Owner', error_correction = 0.0):
        '''
        Assigns value attributes to the class object
        
        Parameters:
            file_path (a string): a file
            last_update_date (a string, optional): the last update date in
            format "dd/mm/yyyy"
            owner (a string, optional): owner of the QR code
            error_correction (a float, optional): the number of error
            correction
        
        Examples:
        >>> my_qrcode = QRCode("qrcode_binary.txt", "01/09/2024", "Vivian",0.1)
        >>> my_qrcode.last_update_date['Day']
        '01'
        >>> my_qrcode.last_update_date['Month']
        '09'
        >>> my_qrcode.last_update_date['Year']
        '2024'
        >>> my_qrcode.owner
        'Vivian'
        >>> my_qrcode.error_correction
        0.1
        >>> my_qrcode = QRCode("qrcode_binary.txt", owner = "Vivian",
        error_correction = 0.1)
        >>> my_qrcode.last_update_date['Day']
        '01'
        >>> my_qrcode.last_update_date['Month']
        '09'
        >>> my_qrcode.last_update_date['Year']
        '0000'
        >>> my_qrcode.owner
        'Vivian'
        >>> my_qrcode.error_correction
        0.1
        >>> >>> my_qrcode = QRCode("qrcode_binary.txt", owner = 'Lacy')
        >>> my_qrcode.last_update_date['Day']
        '01'
        >>> my_qrcode.last_update_date['Month']
        '09'
        >>> my_qrcode.last_update_date['Year']
        '0000'
        >>> my_qrcode.owner
        'Lacy'
        >>> my_qrcode.error_correction
        0.0
        
        '''
        data_list = helper.get_data(file_path)
        self.data = txtdata.TxtData(data_list)
        
        self.last_update_date = helper.convert_date(last_update_date)
        self.owner = owner
        self.error_correction = error_correction
        
    def __str__ (self):
        '''
        Returns a string with a bried description of the QR code
        
        Parameters:
            None
            
        Results:
            string (a string): a string of the given format
        
        Examples:
        >>> my_qrcode = QRCode("qrcode_binary.txt", "01/09/2024", "Vivian",0.1)
        >>> print(my_qrcode)
        The QR code was created by Vivian and last updated in 2024.
        The details regarding the QR code file areas follows:
        This TxtData object has 33 rows and 33 columns.
        >>> my_qrcode = QRCode("qrcode_binary.txt", "0/0/2024", "Vivian",0.1)
        >>> print(my_qrcode)
        Traceback (most recent call last):
        ValueError: Input format incorrect!
        >>> my_qrcode = QRCode("qrcode_binary.txt", "01/01/2024",
        error_correction = 0.1)
        >>> print(my_qrcode)
        The QR code was created by Default Owner and last updated in 2024.
        The details regarding the QR code file areas follows:
        This TxtData object has 33 rows and 33 columns.
        
        '''
        owner = self.owner
        last_update_date = str(self.last_update_date['Year'])
        string = 'The QR code was created by ' + owner + ' and last updated '\
                 + 'in ' + last_update_date + '.\n' +'The details regarding '\
                 'the QR code file are as follows:\n' + str(self.data)
        
        return string
        

    def equals (self, another_qrcode):
        '''
        Returns whether or not two QR codes are the same by evaluating if the
        data and the error_correction attributes are the same.
        
        Parameters:
            another_qrcode (a QR code): a QR code
        
        Results:
            True or False (a boolean): indicates whether the two QR codes are
            the same
        
        Examples:
        >>> my_qrcode = QRCode("qrcode_binary.txt", "01/09/2024", "Vivian",0.1)
        >>> my_qrcode_copy =QRCode("qrcode_binary_copy.txt", "01/09/2022",
        "Xuanpu",0.1)
        >>> my_qrcode.equals(my_qrcode_copy)
        True
        >>> my_qrcode = QRCode("qrcode_binary.txt", owner = 'Vivian)
        >>> my_qrcode_copy =QRCode("qrcode_binary_copy.txt", "01/09/2022",
        "Xuanpu",0.1)
        >>> my_qrcode.equals(my_qrcode_copy)
        False
        >>> my_qrcode = QRCode("qrcode_binary.txt", owner = "Vivian",0.1)
        >>> my_qrcode_copy =QRCode("qrcode_binary_copy.txt",
        last_update_date = "01/09/2022")
        >>> my_qrcode.equals(my_qrcode_copy)
        True
        
        '''
        return self.data.equals(another_qrcode.data) and \
               self.error_correction == another_qrcode.error_correction
        

    def is_corrupted (self, precise_qrcode):
        '''
        Returns whether or not a QR code (self object) is corrupted by
        comparing it with a precise QR code
        
        Parameters:
            precise_qrcode (a QR code): a QR code
        
        Results:
            True or False (a boolean): indicates whether the QR code is
            corrupted
        
        Examples:
        >>> my_qrcode = QRCode("qrcode_binary.txt", "01/09/2024", "Vivian", 0.1)
        >>> my_c_qrcode = QRCode("qrcode_binary_c.txt", "01/09/2000", "Vivian",
        0.1)
        >>> my_c_qrcode.is_corrupted(my_qrcode)
        True
        >>> my_qrcode = QRCode("qrcode_binary.txt", "00/00/0000", "Alex", 0.1)
        >>> my_c_qrcode = QRCode("qrcode_binary_c.txt", "00/00/0000", "Alex",
        0.1)
        >>> my_c_qrcode.is_corrupted(my_qrcode)
        True
        >>> my_qrcode = QRCode("qrcode_binary.txt", "10/03/2000", "Rebecca", 0.1)
        >>> my_c_qrcode = QRCode("qrcode_binary_c.txt", "10/03/2000", "Rebecca",
        0.1)
        >>> my_c_qrcode.is_corrupted(my_qrcode)
        True
        
        '''
        return self.data.approximately_equal(precise_qrcodedata,\
                                             self.data.error_correction)
