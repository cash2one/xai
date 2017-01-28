

#calss header
class _ALARMED():
	def __init__(self,): 
		self.name = "ALARMED"
		self.definitions = [u'worried or frightened by something: ', u'An alarmed vehicle or place has an alarm in it that, when active, will make a loud noise if anyone enters or touches it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
