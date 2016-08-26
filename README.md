api/v1/register/                - Register new User

api/v1/project/                 - List of projects + Create project

api/v1/project/(?P<pk>[0-9]+)/  - Update/Delete Project

api/v1/task/                    - List of tasks + Create task

api/v1/task/(?P<pk>[0-9]+)/$'   - Update/Delete Task

api/v1/user/                    - List of Users(Developers only) + Create User

api/v1/user/(?P<pk>[0-9]+)/     - Update/Delete User

api/v1/project-users            - # M2M between project and user models (Assign project to user and vice versa)

Djangorestframework has built-in functionality of login/logout so I used it.

Djangorestframework hasn't buit-in 'register' functionality so I added it

After register you will have Developer's Account.

System has two roles of users : Manager and Developer. SuperUser equal to  Manager.

Managers can make CRUD operations on the User/Task/Projects

Developers can make Read operations on User/Task/Projects
I put IsAuthenticatedOrReadOnly  into Rest settings  for convinience so if you are not
authenticated user you will have same priviledges as Developer user.

python manage.py createsuperuser - in order to create initial superUser=Manager.

I didn't got the 9 paragraph of the task about celery task
So I implemented the periodic task which send emails
into console for users who had task with due_date = Today.

The code is mostly without comments.=(

