

#calss header
class _OPEN():
	def __init__(self,): 
		self.name = "OPEN"
		self.definitions = [u'not closed or fastened: ', u'ready to be used or ready to provide a service: ', u'not closed in or covered: ', u'If a computer document or program is open, it is ready to be read or used: ', u'available; not limited: ', u'not secret: ', u'honest and not trying to keep things secret: ', u'not decided or certain: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
