# import graphene
# from fastapi import FastAPI
# from starlette_graphene3 import GraphQLApp
# class Query(graphene.ObjectType):
#     hello = graphene.String(name=graphene.String(default_value="stranger"))
# def resolve_hello(self,info,name):
#         return "Hello " + name
# app = FastAPI(title='ContactQL', description='GraphQL Contact APIs', version='0.1')
# @app.get("/")
# async def root():
#     return {"message": "Contact Applications!"}
# app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query)))


from fastapi import FastAPI
from graphene import ObjectType, List, String, Schema
from starlette.graphql import GraphQLApp
from schemas import CourseType,CreateCourse
import json

class Query(ObjectType):
    course_list = None
    get_course = List(CourseType)
    def resolve_get_course(self, info):
        with open("./courses.json") as courses:
            course_list = json.load(courses)
        return course_list
    
class Mutation(ObjectType):
    create_course = CreateCourse.Field()
    
    
app = FastAPI()
app.add_route("/", GraphQLApp(schema=Schema(query=Query, mutation=Mutation)))