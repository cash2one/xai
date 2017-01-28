

#calss header
class _IMPERFECT():
	def __init__(self,): 
		self.name = "IMPERFECT"
		self.definitions = [u'damaged, containing problems, or not having something: ', u'The imperfect form of a verb describes an action in the past that was continuous or was not completed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
