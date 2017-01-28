

#calss header
class _RUGGED():
	def __init__(self,): 
		self.name = "RUGGED"
		self.definitions = [u'(of land) wild and not even; not easy to travel over: ', u'strong and simple; not delicate: ', u"If a man's face is rugged, it is strongly and attractively formed: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
