from graphene import String, ObjectType, Mutation,Field
import json

class CourseType(ObjectType):
    id = String(required=True)
    title = String(required=True)
    instructor = String(required=True)
    publish_date = String()
    
class CreateCourse(Mutation):
    course = Field(CourseType)
    
    class Arguments:
        id = String()
        title = String()
        instructor = String()
        publish_date = String()
        
    def mutate(self, info, id , title, instructor, publish_date):
        new_entry = {}
        new_entry["id"] = id
        new_entry["title"] = title
        new_entry["instructor"] = instructor
        new_entry["publish_date"] = publish_date
        with open("./courses.json", "r") as courses:
            course_list = json.load(courses)
        course_list.append(new_entry)
        with open("./courses.json", "w") as courses:
            json.dump(course_list, courses, indent=4)
            
        return CreateCourse(course=course_list[-1])
        
        