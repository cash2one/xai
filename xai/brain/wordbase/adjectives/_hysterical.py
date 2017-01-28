

#calss header
class _HYSTERICAL():
	def __init__(self,): 
		self.name = "HYSTERICAL"
		self.definitions = [u'unable to control your feelings or behaviour because you are extremely frightened, angry, excited, etc.: ', u'extremely funny: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
