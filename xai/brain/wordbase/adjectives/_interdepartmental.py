

#calss header
class _INTERDEPARTMENTAL():
	def __init__(self,): 
		self.name = "INTERDEPARTMENTAL"
		self.definitions = [u'between or involving different departments of a school, university, business, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
