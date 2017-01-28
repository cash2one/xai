

#calss header
class _UNGENTLEMANLY():
	def __init__(self,): 
		self.name = "UNGENTLEMANLY"
		self.definitions = [u"(of a man's behaviour) not polite and not behaving well towards other people: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
