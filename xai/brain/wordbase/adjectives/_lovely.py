

#calss header
class _LOVELY():
	def __init__(self,): 
		self.name = "LOVELY"
		self.definitions = [u'pleasant or enjoyable: ', u'beautiful: ', u'used to describe a person who is kind, friendly, and pleasant to be with: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
