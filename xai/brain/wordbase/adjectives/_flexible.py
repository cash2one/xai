

#calss header
class _FLEXIBLE():
	def __init__(self,): 
		self.name = "FLEXIBLE"
		self.definitions = [u'able to change or be changed easily according to the situation: ', u'able to bend or to be bent easily without breaking: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
