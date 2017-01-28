

#calss header
class _DEEP():
	def __init__(self,): 
		self.name = "DEEP"
		self.definitions = [u'going or being a long way down from the top or surface, or being of a particular distance from the top to the bottom: ', u'very strongly felt or experienced and usually lasting a long time: ', u'(of a sound) low: ', u'showing or needing serious thought, or not easy to understand: ', u'If something is deep, it has a large distance between its edges, especially between its front and back edges: ', u'near the middle of something, and a long distance from its edges: ', u'(of a colour) strong and dark: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
