class Profile:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        
    def __str__(self) -> str:
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'
        
    @property
    def username(self) -> str:
        return self.__username
    
    @username.setter
    def username(self, value: str) -> None:
        if not 5 < len(value) < 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        
        self.__username = value
        
    @property
    def password(self) -> str:
        return self.__password
    
    @password.setter
    def password(self, value: str) -> None:
        is_valid_length = len(value) >= 8
        is_upper_existing = len([x for x in value if x.isupper()]) > 0
        is_digit_existing = len([x for x in value if x.isdigit()]) > 0
        
        if not (is_valid_length and is_upper_existing and is_digit_existing):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
            
        self.__password = value
        
        
#profile_with_invalid_password = Profile('My_username', 'My-password')
#profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)