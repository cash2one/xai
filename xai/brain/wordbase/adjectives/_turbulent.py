

#calss header
class _TURBULENT():
	def __init__(self,): 
		self.name = "TURBULENT"
		self.definitions = [u'involving a lot of sudden changes, arguments, or violence: ', u'Turbulent air or water moves very strongly and suddenly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
