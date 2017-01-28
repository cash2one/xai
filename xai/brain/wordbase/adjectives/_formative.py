

#calss header
class _FORMATIVE():
	def __init__(self,): 
		self.name = "FORMATIVE"
		self.definitions = [u'relating to the time when someone or something is starting to develop in character: ', u'A formative assessment happens while a student is being taught about a subject, rather than at the end of a year or unit of work, in order to check their progress: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
