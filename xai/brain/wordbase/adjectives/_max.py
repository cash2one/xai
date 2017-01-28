

#calss header
class _MAX():
	def __init__(self,): 
		self.name = "MAX"
		self.definitions = [u'informal for  maximum adjective , often used after an amount: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
