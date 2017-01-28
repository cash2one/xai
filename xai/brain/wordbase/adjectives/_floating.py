

#calss header
class _FLOATING():
	def __init__(self,): 
		self.name = "FLOATING"
		self.definitions = [u'not fixed in one position, place, or level: ', u'used to refer to a part of the body that is out of its usual position, or not connected to another part of the body: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
