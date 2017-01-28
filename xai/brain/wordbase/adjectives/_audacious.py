

#calss header
class _AUDACIOUS():
	def __init__(self,): 
		self.name = "AUDACIOUS"
		self.definitions = [u'showing a willingness to take risks or offend people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
