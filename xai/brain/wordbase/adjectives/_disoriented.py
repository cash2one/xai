

#calss header
class _DISORIENTED():
	def __init__(self,): 
		self.name = "DISORIENTED"
		self.definitions = [u'confused and not knowing where to go or what to do: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
