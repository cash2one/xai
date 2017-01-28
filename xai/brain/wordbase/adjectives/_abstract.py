

#calss header
class _ABSTRACT():
	def __init__(self,): 
		self.name = "ABSTRACT"
		self.definitions = [u'existing as an idea, feeling, or quality, not as a material object: ', u'An abstract argument or discussion is general and not based on particular examples: ', u'general ideas: ', u'used to refer to a type of painting, drawing, or sculpture that uses shapes, lines, and colour in a way that does not try to represent the appearance of people or things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
