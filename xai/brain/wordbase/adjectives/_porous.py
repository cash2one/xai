

#calss header
class _POROUS():
	def __init__(self,): 
		self.name = "POROUS"
		self.definitions = [u'Something that is porous has many small holes, so liquid or air can pass through, especially slowly: ', u'not protected enough to stop people going through: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
