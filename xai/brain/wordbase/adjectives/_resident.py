

#calss header
class _RESIDENT():
	def __init__(self,): 
		self.name = "RESIDENT"
		self.definitions = [u'living or staying in a place: ', u'used to refer to someone who has a special skill or quality in a group or organization: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
