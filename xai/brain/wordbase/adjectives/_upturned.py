

#calss header
class _UPTURNED():
	def __init__(self,): 
		self.name = "UPTURNED"
		self.definitions = [u'pointing or looking up, or having the part that is usually at the bottom turned to be at the top: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
