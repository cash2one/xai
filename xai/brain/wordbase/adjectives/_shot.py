

#calss header
class _SHOT():
	def __init__(self,): 
		self.name = "SHOT"
		self.definitions = [u'(of silk) having small threads of a colour in it, so that the main colour appears to change depending on the angle at which the cloth is seen: ', u'no longer working or effective: ', u'to get rid of or free of something, or to leave something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
