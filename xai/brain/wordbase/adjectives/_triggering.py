

#calss header
class _TRIGGERING():
	def __init__(self,): 
		self.name = "TRIGGERING"
		self.definitions = [u'causing someone to feel upset and frightened because they are made to remember something bad that has happened in the past: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
