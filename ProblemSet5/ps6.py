import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story
    
def decrypt_story():
    """"
    Returns: the story decrypted
    """
    encrypted = get_story_string()
    
    decrypted = CiphertextMessage(encrypted)
    
    return decrypted.decrypt_message()

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
    
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26
    
        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        low_case = string.ascii_lowercase
        upper_case = string.ascii_uppercase
    
        shift_val = shift
    
        all_casesShift = {}
    
        if shift == 26:
            raise IndexError('Shift value must be under 26')
    
        for i in low_case:
            all_casesShift[i] = low_case[shift_val]
            shift_val = shift_val + 1
            if shift_val == 26:
                shift_val = 0
    
        shift_val = shift
    
        for i in upper_case:
            all_casesShift[i] = upper_case[shift_val]
            shift_val = shift_val + 1
            if shift_val == 26:
                shift_val = 0
    
        return all_casesShift

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26
    
        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        
        message_text = self.message_text
        
        ignored = ' ' + string.punctuation + string.digits
        
        dicShift = self.build_shift_dict(shift)
        
        shifted_message = ''
        
        for i in message_text:
            if i in ignored:
                shifted_message = shifted_message + i
            elif i in dicShift:
                shifted_message = shifted_message + dicShift[i]
                
        return shifted_message

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        Message.__init__(self, text)
        self.shift = shift

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        self.encrypting_dict_copy = {}
        self.encrypting_dict = self.build_shift_dict(self.shift)
        
        for i in self.encrypting_dict:
            self.encrypting_dict_copy[i] = self.encrypting_dict[i]
        
        return self.encrypting_dict_copy

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        self.message_text_encrypted = self.apply_shift(self.shift)
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        self.message_text = text
#        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        word_shift = 0
        word = ''
        count = count_new = 0
        output_tuple = ()
        
#        message = self.message_text.split(' ')

        for x in range(0,26):
#            print(x)
            word = self.apply_shift(x)
#            print(word)
            message = word.split(' ')
            for i in message:
                if is_word(self.valid_words, i) is True:
                    count = count + 1
                    if count > count_new:
                        count_new = count
                        word_shift = x
            count = 0
        
        output_tuple = output_tuple + (word_shift,)
                    
        word = self.apply_shift(word_shift)
        
        output_tuple = output_tuple + (word,)
            
        return output_tuple


mensagem = 'O, my back, my back, my bach! I\'d want to go to Aches-les-Pains. Pingpong!'

#Example test case (PlaintextMessage)
plaintext = PlaintextMessage(mensagem, 13)
# print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())
    
# Example test case (CiphertextMessage)
ciphertext = CiphertextMessage(mensagem)
# print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())
