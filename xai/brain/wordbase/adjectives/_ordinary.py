

#calss header
class _ORDINARY():
	def __init__(self,): 
		self.name = "ORDINARY"
		self.definitions = [u'not different or special or unexpected in any way; usual: ', u'normally, or in the way that usually happens: ', u'unusual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
