

#calss header
class _OMNIPOTENT():
	def __init__(self,): 
		self.name = "OMNIPOTENT"
		self.definitions = [u'having unlimited power and able to do anything: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
