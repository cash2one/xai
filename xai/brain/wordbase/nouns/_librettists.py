

from xai.brain.wordbase.nouns._librettist import _LIBRETTIST

#calss header
class _LIBRETTISTS(_LIBRETTIST, ):
	def __init__(self,): 
		_LIBRETTIST.__init__(self)
		self.name = "LIBRETTISTS"
		self.specie = 'nouns'
		self.basic = "librettist"
		self.jsondata = {}
