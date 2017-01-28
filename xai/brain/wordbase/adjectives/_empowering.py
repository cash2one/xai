

#calss header
class _EMPOWERING():
	def __init__(self,): 
		self.name = "EMPOWERING"
		self.definitions = [u'Something that is empowering makes you more confident and makes you feel that you are in control of your life: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
