from my_functions import *
def checkResponse(response):
    '''
        A error checking function to check API request success. \n
        Returns True / False
    '''
    if response.status_code == 200:
        print("Response received successfully! \nAPI is functioning")
        #lfi("Response received successfully! - API is functioning")
        
        return True
    else:
        print(f"Error: Failed to receive response (Status Code: {response.status_code})")
        #lfd(f"Error: Failed to receive response (Status Code: {response.status_code})")
        print("Check the API")
        #lfd("The API did not respond. Exception: TO DO")
        return False
    
def checkAPI():
    '''
        A function to check if API is working. \n
    '''
    
### todo: test logging , test json