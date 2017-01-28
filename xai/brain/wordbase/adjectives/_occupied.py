

#calss header
class _OCCUPIED():
	def __init__(self,): 
		self.name = "OCCUPIED"
		self.definitions = [u'An occupied place is being controlled by an army or group of people that has moved into it: ', u'being used by someone; with someone in it: ', u'busy or interested: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
