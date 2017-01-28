

#calss header
class _QUAINT():
	def __init__(self,): 
		self.name = "QUAINT"
		self.definitions = [u'attractive because of being unusual and especially old-fashioned: ', u'Quaint can also be used to show that you do not approve of something, especially an opinion, belief, or way of behaving, because it is strange or old-fashioned: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
