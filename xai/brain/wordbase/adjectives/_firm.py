

#calss header
class _FIRM():
	def __init__(self,): 
		self.name = "FIRM"
		self.definitions = [u'not soft but not completely hard: ', u'well fixed in place or position: ', u'fixed at the same level or opinion and not changing: ', u'strong and tight: ', u'certain and not likely to change: ', u'forceful and making people do what you want: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
