

#calss header
class _BACKHANDED():
	def __init__(self,): 
		self.name = "BACKHANDED"
		self.definitions = [u'A backhanded remark seems pleasant but may really be a criticism or mean something unkind: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
