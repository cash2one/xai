

#calss header
class _LEWD():
	def __init__(self,): 
		self.name = "LEWD"
		self.definitions = [u'(of behaviour, speech, dress, etc.) sexual in an obvious and rude way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
