

#calss header
class _ALERT():
	def __init__(self,): 
		self.name = "ALERT"
		self.definitions = [u'quick to see, understand, and act in a particular situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
