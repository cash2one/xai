

#calss header
class _RUTTED():
	def __init__(self,): 
		self.name = "RUTTED"
		self.definitions = [u'If a surface is rutted, it has deep narrow marks in it made by wheels: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
