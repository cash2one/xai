

#calss header
class _VENTURESOME():
	def __init__(self,): 
		self.name = "VENTURESOME"
		self.definitions = [u'used to describe a person who is willing to take risks, or an action or behaviour that involves risks: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
