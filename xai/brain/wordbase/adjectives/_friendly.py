

#calss header
class _FRIENDLY():
	def __init__(self,): 
		self.name = "FRIENDLY"
		self.definitions = [u'behaving in a pleasant, kind way towards someone: ', u'A friendly place is pleasant and makes you feel happy and comfortable: ', u'A friendly game or argument is one that you play or have for pleasure and in order to practise your skills, rather than playing or arguing seriously with the aim of winning: ', u'Friendly countries and friendly soldiers are ones who are not your enemies and who are working or fighting with you.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
