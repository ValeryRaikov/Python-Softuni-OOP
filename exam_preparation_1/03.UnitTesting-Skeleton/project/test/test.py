from unittest import TestCase, main

from project.movie import Movie


class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie("Oppenheimer", 2023, 8.4)
    
    def test_movie_initialized_correctly(self):
        self.assertEqual("Oppenheimer", self.movie.name)
        self.assertEqual(2023, self.movie.year)
        self.assertEqual(8.4, self.movie.rating)
        self.assertEqual([], self.movie.actors)
        
    def test_movie_empty_string_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.name = ""
            
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_movie_incorrect_year_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.year = 1850
            
        self.assertEqual("Year is not valid!", str(ex.exception))
        
    def test_add_actor_method_list_extension_expected(self):
        self.assertEqual([], self.movie.actors)
        
        self.movie.actors.append("Cillian Murphy")
        
        self.assertEqual(["Cillian Murphy"], self.movie.actors)
        
    def test_add_actor_method_actor_already_in_list_message_expected(self):
        self.movie.add_actor("Cillian Murphy")
        
        self.assertEqual("Cillian Murphy is already added in the list of actors!", self.movie.add_actor("Cillian Murphy"))
        
    def test_greater_than_method_compares_correctly(self):
        test_movie = Movie("Barbie", 2023, 9.1)
        
        self.assertEqual('"Barbie" is better than "Oppenheimer"', self.movie.__gt__(test_movie))
        self.assertEqual('"Barbie" is better than "Oppenheimer"', test_movie.__gt__(self.movie))
        
        test_movie = Movie("Barbie", 2023, 8.1)
        
        self.assertEqual('"Oppenheimer" is better than "Barbie"', test_movie.__gt__(self.movie))
        self.assertEqual('"Oppenheimer" is better than "Barbie"', self.movie.__gt__(test_movie))
        
    def test__repr__method_return_correct_message(self):
        self.movie.add_actor("Cillian Murphy")
        self.movie.add_actor("Robert Downey Jr.")
        
        self.assertEqual(
            "Name: Oppenheimer\n" \
            "Year of Release: 2023\n" \
            "Rating: 8.40\n" \
            "Cast: Cillian Murphy, Robert Downey Jr.",
            self.movie.__repr__()
        )    
    

if __name__ == "__main__":
    main()