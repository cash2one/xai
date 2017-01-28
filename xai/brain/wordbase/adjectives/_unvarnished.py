

#calss header
class _UNVARNISHED():
	def __init__(self,): 
		self.name = "UNVARNISHED"
		self.definitions = [u'An unvarnished statement is expressed in a plain and honest way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
