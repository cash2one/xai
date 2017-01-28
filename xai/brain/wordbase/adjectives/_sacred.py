

#calss header
class _SACRED():
	def __init__(self,): 
		self.name = "SACRED"
		self.definitions = [u'considered to be holy and deserving respect, especially because of a connection with a god: ', u'connected with religion: ', u'considered too important to be changed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
