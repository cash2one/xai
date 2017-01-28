

#calss header
class _SUPPLE():
	def __init__(self,): 
		self.name = "SUPPLE"
		self.definitions = [u'bending or able to be bent easily; not stiff: ', u'able to change quickly and successfully to suit different conditions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
