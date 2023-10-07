from project.student import Student

from unittest import TestCase, main


class TestStudent(TestCase):
    def setUp(self) -> object:
        self.student1 = Student("s_with_courses", {"maths": ["math is fun", "zero to hero"]})
        self.student2 = Student("s_without_courses")
        
    def test_students_initialized_correctly(self):
        # first student
        self.assertEqual("s_with_courses", self.student1.name)
        self.assertEqual({"maths": ["math is fun", "zero to hero"]}, self.student1.courses)
        
        #second student
        self.assertEqual("s_without_courses", self.student2.name)
        self.assertEqual({}, self.student2.courses)
        
    def test_course_name_in_students_courses_update_notes_expected_return_correct_message(self):
        course_name = "maths"
        notes = ["more notes", "geometry is shit"]
        
        result = self.student1.enroll(course_name, notes)
        
        self.assertEqual({"maths": ["math is fun", "zero to hero", "more notes", "geometry is shit"]}, self.student1.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)
        
    def test_add_course_notes_works_properly_return_correct_message(self):
        course_name = "chemistry"
        notes = ["organic", "basic interactions"]
        add_course_notes = "Y"
        
        result = self.student2.enroll(course_name, notes, add_course_notes)
        
        self.assertEqual({"chemistry": ["organic", "basic interactions"]}, self.student2.courses)
        self.assertEqual("Course and course notes have been added.", result)
        
    def test_add_course_without_notes_extend_dictionary_expected_return_correct_message(self):
        course_name = "chemistry"
        notes = ["organic", "basic interactions"]
        add_course_notes = "test note"
        
        result = self.student2.enroll(course_name, notes, add_course_notes)
        
        self.assertEqual({"chemistry": []}, self.student2.courses)
        self.assertEqual("Course has been added.", result)
        
    def test_add_notes_method_raises(self):
        course_name = "history"
        notes = ["history is boring"]
        
        with self.assertRaises(Exception) as ex:
            self.student1.add_notes(course_name, notes)
            
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))
        
    def test_add_notes_method_adds_return_correct_message(self):
        course_name = "maths"
        notes = ["more notes", "geometry is shit"]
        
        result = self.student1.add_notes(course_name, notes)
        
        self.assertEqual({"maths": ["math is fun", "zero to hero", ["more notes", "geometry is shit"]]}, self.student1.courses)
        self.assertEqual("Notes have been updated", result)
        
    def test_leave_course_method_raises(self):
        course_name = "programming basics"

        with self.assertRaises(Exception) as ex:
            self.student2.leave_course(course_name)
            
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
        
    def test_leave_course_method_leaves_return_correct_message(self):
        course_name = "maths"
        
        result = self.student1.leave_course(course_name)
        
        self.assertEqual({}, self.student1.courses)
        self.assertEqual("Course has been removed", result)
        

if __name__ == "__main__":
    main()