#!yaml|gpg

environment: production

domain: re-volv.org

repo:
  url: git@github.com:RE-volv/revolv.git
  branch: master

# Addtional public environment variables to set for the project
env:
    NEW_RELIC_APP_NAME: re-volv production
    NEW_RELIC_MONITOR_MODE: "true"

# Uncomment and update username/password to enable HTTP basic auth
# Password must be GPG encrypted.
#http_auth:
#    "re-volv": |-
#      -----BEGIN PGP MESSAGE-----
#      Version: GnuPG v1
#
#      hQEMA9aTfmR7xthMAQf/UFIc+RjmHlOO6H7bT0MFD+BktB8m7l0QYBNjvSrENYwO
#      VLDEp5bLY60QaxDwEP27g2O8SiL670FRLHPvAHN4j44ddQkMT3DUUDYeWWJ1nFiA
#      Z6m+B5sh4MGOVneEjNOnFFP9rBZYVkjlTbE2YH2i83GR4iTUBa1X6htznxBUv9dT
#      hkDe0u7ZMa1qaPOvdxAUxqGTIYMmOESzRL7fHywh4zriyr0Ybplg/o7AzxXUK99K
#      e72yPzxnfz+w2xpk3KesSbLwoTF5woTS2kjtgQVWbQErOK9ggUCV60RLyXNl7O64
#      ThEjFTPxMvWFjhZHDoOxZXyU2ZEZKJ2QrfW9FWMqZ9JHAayP2hE6/1VtzsjoUK3K
#      DYigbUk9JSgki44oP291MuH5dE4gOoaWNMMR006HYEpYCd7I/pO+jjFp11P088Q5
#      Foo3Py/qT4Y=
#      =aHwb
#      -----END PGP MESSAGE-----

# Private environment variables.
# Must be GPG encrypted.
secrets:
    "DB_PASSWORD": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf9G13NuXlim8Bx3LsS6ydmFV6ioatixkXx0XOedwG7poV8
      Du0+/WGDO0umyD2C7X5pfZmmHWXVLw9gg3qJiJtsExUJkkvBsdUL6vjE87W8IDMb
      ibGvz95IBFDba6jRanymVfNNu27117v0fhKF8YEFHpl55zfg6uIIzM7CXrycfvFJ
      m3LNT8iaR8mCm4soBSHiqAYx0tSOhmbKqF7kjFmk4kugFd1rJHRHjEOt86EkM6vz
      1c4nBOAniG/WU96yOm41EiSQt/rwrzQ2daZSZH6iUYn/WgjIn52wjttuHFC+cY6h
      2OKydgQqodz3TzrAM2bztclSBvh/f9BMe392OjHVt9J7ARF1jva1Oqviq/nRRbf8
      GCwMnKPRNkdWUj40T2GnyQ0qenNkL9KQifR4A1GThCtwTWCfbXxFSn5JdSI8hpi8
      2QnoeQDeGu3JQbD1t6ukTUDwmdk0ZZfd26J+xMeSiiWKGZ6wkEz67Tb41iTSOFHr
      QJOdl4kYRMC1HIl7
      =duZ5
      -----END PGP MESSAGE-----

    "MAILCHIMP_API_KEY": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQgAnojpr0q+/OCSKoggut8KdjsQnquVN+NkEMvqxvbUQKx3
      JNVG0vznitIUpFXFI5jARy7AAnWIWecc6nMMachSjxmPio5ziIu+HBifmxWldxAS
      ZdS2DP4DTcCqKs4Q8GZmhN2ToRsrY/JImnD5WV88gYBCdTM4sR048RktQVxxjQIc
      +gRiboarUU91Nrl1esRSfeBGbYqoQPraApJSq6SIY6/zNU8AihJdHEH5UPthbqrf
      WJ5Vg4JyT+0BH1AMPAOhXB74A+ITnoDlaM1mcvO6NG3gOJETiKGtSd090B88/Aas
      xPIn+It1GSWvSYGODfYurZSCIk3gmb4M3V7EVJjmRdJRAd3e2NtFJ+eFEd3uiSW7
      fuvPbwsLlH42Dyipung8zVQphpoei/ESyHxJUlkyjomlghfiWhP5qgeOSBCKjasL
      Upu+RxV1pHVBsDjbblnvwQzf
      =g9gI
      -----END PGP MESSAGE-----

    "SECRET_KEY": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf/ZfjG6x8fdbPdB84x4XkkYRYVVBLG9x/qVwWtKXiQ0Lrr
      kvmm1kkadYdINngwYWvQmMB3IAUTCgyTT7rvvg9Bv/8h20eFWKhvRIh6HZ4yDVu2
      1oHj17el4gVYmKYXI2h0uvvHC7/F0fW6b6eoAGs5+i9a2dHnksGpZA4JlC0f8Oov
      lwOADclknR2L5IOxeax5frHGT1IN2bB/bEK72M4JMTTTVhy+MAmffUoZEgwCJe1l
      fw/qvVBt44TGcUSkj7N0YMqj//7bPnfGQa95ngYwlfhZYioWHFtXuL2MLYtMyr8h
      1eUJ6mnxMTzEn8H8Hy3gFmfE7HnoJ96rMlSrrkRi/tJ7AQq3tb1WA3LNjIk3k9rE
      g3jKUSV+OTMqzrGVa4Qj159QmUW2MDgW6yV+lH6Omd7qp7FG/YyIi3BZfh5+jrgp
      4Sf4BivOJncHafqtxFmpLfufUfqdf/9S0jOvSMgIgjBS8cRRdB5ua3OB4nAM8D5+
      wr+jJZlwxQQW4uQ8
      =rCe3
      -----END PGP MESSAGE-----

    "BROKER_PASSWORD": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf/f4NUZVT3RWOGh4p+3xFJ02xX9FpmZkf3kAveIg1bltiZ
      TeLAW9FJjVvh1I5TLZrrII/rYczckF/EOThhCHwLrp5sMbPy8gnYyiSUrL/Bv5Zq
      AwxPmCBPb04gjEbZNUwKKyWHmx8uKnreb6/rsfHDhxflr7xUk2M2VtEmza/RDjf2
      hJiwMx1TKXd+4C72kPQ+dvyFvPlCFkReE/CLFBZmKalS/yIL1tPPbVzJ2E+0i7Vv
      bYelD+Vve1h28DvOmPAp6XnVHpSViiE++zyJq77x2gXvsja6/3bZn9K194WYZk2I
      TNFUznk3vPSVRdzzGfGcjgMNEDaN2ZvbTUPaozNjidJ7ARrijwcUVKHHEJVypueJ
      QP7JXxYcfnn1TItDNk4MVi263UOZvuDXZY8UiE5C3QSuo/0Db/xsvzzgrv71p+Z0
      8UmlrSgGq2wAXSGoomffEQExn6Dj2bTKIAVKWvtKbStLJi2ZefSIghZVYdv4tpTT
      830oMCwnOkqOEcyz
      =b/1z
      -----END PGP MESSAGE-----

    "NEW_RELIC_LICENSE_KEY": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf8CdmomEDvs0aq7jesJRyxsSEwBe+PUgBa/gBfjWS9ZPiR
      yJEuyhn00VUzQMp+mGEwJVfT8jZ55PcO8texLhvQPEnEk3B/h4+hOL8gT8AnCnfT
      moYcqYFcBdnq12iu5j3miCatHDdl7mPWckKIFlHmhAVjFt56eknnQHndBxNqxhxj
      IdudML7Ugrx2iY2DUfAsmDf9tVxoCnCX00yQwY0uOAuMAXLZhs0CRHyrLVNEqnRi
      h+cQzSiQJgA5sKqwMnkkljhaeMU6DskZOg2hKfGUzZjsvqersT04adZ0OSlxzTD5
      pl3AlCYjTU16EYv+9cJ2DBx7rntPRiPF1OrwT1T2bdJjATnFNvA7xvwtuGV/d5gG
      rqJjH8Yr1j/EQpb2LEkIyNYT9uq1a23sUzh+OhjS8fjvwQxfRZxfH0t4SC3aPmgA
      s4QeQFqdD02/LG8vyzd5yHrmYnO50TTKnMuyk8VWv2GgrGsV
      =9z5X
      -----END PGP MESSAGE-----

    "LOG_DESTINATION": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf/XImTyudxieMRl1Qh0viuEtqWfbXZMYY482KHFBHLzKWB
      dFBFideQH5sibM3iqo8+L+fA4tpHEiXFyDiCKNV2u5o93kTwdNE20r2NcQ5zTA0r
      Xqono66vJUyVWbl4NSd608HH9vRSCmDxNM+R7hJ75V/fXRXINJFhIZiDaeNKvr7W
      dm2AbKX/lbsJSLf/KFqHY4KJLFqcClMOL9c6CFOAAxYGgSAYN7YPn5ThIU78vomH
      2uej6eioSpdavHJQvvb7DYph5C1J9M8MOd0dSvLwv/YE5yVwen8LAOQuicplFfWQ
      WKm7Vw9LemvOEXcHJf+XAaSIQDky2filDfaane3cpNJYAb0WQu3/cKfhZO7nZnAs
      82u+YBP9lQPPCT7fYNvyEQin+1rJDsdv9hrKg8arWnQO1FyhjKZuiT0ZU7d8GX1H
      PCzyZp7J10n8oIWeBZputJN4vOMh/Aq8Ew==
      =ZhYg
      -----END PGP MESSAGE-----

    "SOCIAL_AUTH_FACEBOOK_KEY": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQgAyxPm+UvTNAtzp7s4bLhijXMRzULgATrHYtnKILdJWJkm
      vLXZzNUZrorDsvnnoV0YC+5Ynj8BqupzwFb/lwuNApseywmhYaJGZkQH+LoLfBge
      ti/B6RGpDgnjeIQRwdv4KEP0Szay4Fz5m6DeqbumdGmQWtC+Cat/9tZoWdcJTve7
      Z3u+rCInYXzoysz5XsVxk+vuoeg84536KgFYj0REUdLPJO8OQzseJ9enkRsGdjlm
      ZTaM4q+0Ht+jEqCJjyp9vpLSu+sJ8aRW3sR3NHVVH5ZCYocmKQigKaTkj6fJOOJN
      wHOjlEmoL4LtdwsG61vSi2zyULYk9NHDBn/NXG+LGdJLAejoHwHpTZjBe1nrnF1L
      /h2XEB7Vl7f1DBsL6cuS7UZPFYE3oks/e32G4iAQniy85evAqFHbeoLyVTmG4HYB
      nTHyFBJb7y2yZvDj
      =2JuF
      -----END PGP MESSAGE-----

    "SOCIAL_AUTH_FACEBOOK_SECRET": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf8COMs+oRmM61Rf0kiC9+B/Afoao7icJu2B+582H+nJsTY
      xMkIN7gWn20nnlZzQWIZLVGUc79Lu36Iko+1ks3Jjj5/JG31sWiG30aNcaRFW214
      h0uldqDg+RGzqCpVpKHUl47q9TBs/Lzi9Swc/XczU68rZc0I9vQHWTc0Q94RkbTb
      4M4+aVdACQjjgd5shyrdX7dpotqRhTrSFthwdBldFXT0mB8IyD91mpKL+cBChwvX
      oi1VnahiRxW3FbE/J5GjA5kgnckF9rIYAE1O0KZWoiBKa43MVzYX+ToFjakowwRv
      nm0WfRV0sw89uHsBjtEOKfK4vSkZY23voXNm22wDvtJbARaBIQjaDuBADHxJXvRv
      nnqmLtgDgryWOu2goTAMwBDWsPCBzaGBzGEd/dPy1PGedbEUc4zjMzxZRbMgLL1v
      sTrOVMTM5b225XaaaKG/80+l/JUXVMkwRfzx7g==
      =hcbB
      -----END PGP MESSAGE-----

    "SOCIAL_AUTH_GOOGLE_OAUTH2_KEY": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v2

      hQEMA9aTfmR7xthMAQgAgkVqADiOB5i9FqZUmxVb8sJ+WY0ZKLNjwUGoRFtfbJ9a
      YVC8AdqbsltGa4UpRCyBlWrF0yRYSGGspNi6M7h3p9oG9ARQP1AG/YOztjEig/Ya
      QEdkDw5gcDKzeu5ZxXoqLcpzaV+M1wfkz0sl5zEa4Anlk5SyvMnyK6qy7xRS/P6j
      sQVBFx7H6f5npAQ4XlFhCCkn38OHA2sm77m557fC/Vfz/jBOSRQ00QgBiNat8Ctt
      QcgDWkrXxY/3NRszkZ9KEtk8HxHwlEe9dOuhmYfD5zOHDXEfIMitSZJ3kzTBg4X3
      twpsRrq1GDZBB415K/LtBIhcbDomb1keW5t5loxH8dKEAZlv/XboXSqJQ7OMKIoF
      iiT7Bi1Yn2nnPyy2AY94ZBVze1SUNI+iKJg9YX6pImBLWPPUZI/r0GthdfWosJev
      YHlVC7MlYi+xqbYghbhBplJM9hVtvawo/4a0XWMojrjWsot2Vo8LSRfyEB+BFZZ5
      g9zEeq3kcAH0pzwQ7soAjnyowSzA
      =Wr4k
      -----END PGP MESSAGE-----

    "SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v2

      hQEMA9aTfmR7xthMAQf/ZwKuQFiVa2mNpRWby3tVhEibo7+Evh4ulwHdJXgoEM70
      fEPQQlu8e9Nx7RpGPBoElC+RmbdcqiD3V1kc2ILc7NBB5Ci3zJny+Dr7wgqID5Uh
      k364/43SuVZsPg1wW3bZh/MxqFEszg3XzvX8YN7H7uizkbn6jVuU2SfCPqNI1+mX
      hoZ7MKZ1M7hb6cjMeJhiJfA15gDnBCD/PgROamDZS54dl9JxsjEsDGNqJIADErE3
      FHGyr5N1a8KjIe/9yPZt2gAGuU47T9T1dARrSU2Dzv1OMNE44mjVfHiV1hP8SWf1
      Gual5FKANWnHF8ZQ6FoFC2R5t3+C+Q+fYD91xlStV9JTAW9THTPrnFfT09kP26do
      /peIis30+euuW8dDs1HfRHwiTntI+1ZysIb94puXzXctQyadHwyuEc6tIBABYgBI
      /9naFeVCvFxlWWjXZbvph35dtXo=
      =kIc2
      -----END PGP MESSAGE-----

    "STRIPE_SECRET_KEY": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQgAoGajf/jECL9UTaQrlP+WSYc5sgZFM/NWaKzJq6bRElWT
      ZnG5Yk7n3nmBB/yIwVu0i6xX4ferPoXFqbeeEUcsczoBPNLGNnxDQNc4UQSstcKu
      6WASMqF5c+xycWrgmOeONO9cVpbt4gZkr3sGm49NAJ5BXunewhJh3Rw6nYElvC6u
      PUfC0QM7n20+gB35sHsggjnktiUW5tx4giiwoqoLGIJJdpkAUtZ7jyEfXirF5nM9
      RihVvt3AJIZ8BrG+6LbeVFWMsuSejCkZ7hQfU6N9qVinEp7VgLIkQf57EE9/XqZo
      LF8+BOHq0NKONfpSU9ptTscpLTQlYpVz1nn6tNGBT9JbAQi8EtS+UUXknkvsHfdz
      SNrbiBAfDMs+hRS75RMurJSMSctK96Cx4abhQ/or0S4SX4ZUnlp+SWV7Jedv31Yx
      L6Nf9XBit4KFfqSBvUmPbMv442C7AfQwmaWUKw==
      =LXhi
      -----END PGP MESSAGE-----

    "STRIPE_PUBLISHABLE": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf+Lqe7JC6a7heBdNgOCpXWzL1Xqcj+G/zqRtXMp59Vflvm
      qrbq2i4kFA9nb7gZbO1WSFEwHpTqc5UuDUMfFsFxhOy/t7oq+7EZ6b4nkxPYppbV
      t6ymGWtKI43c+fKtIvkdqjygMFK8dD9Mhtx+m/B25+ZJJ5aWoFQ83KKoMeFPdjoR
      MbyvEzg6XFYljfLFmDfPo2hqyC83J8QEkyXNwEmLQTeJGlxyBInbIg32c2IvcmsI
      7/u2O+g5UuMQ4etd7Fx4K4prWQXwa2Xodc19jbct3xWqw2ME02E5x+XdmTnANGdj
      af0b0mI1206gZH0C0ymEQk4CkuLipqJSjPiaMJOajtJbAUH6nOGuo5t5luA1atpx
      Z77Pncgb0sE2rJxcAlvj+ScAKRbuCWzLMBz6IYFAZjBvhqZfCNHrD9fc4xEjccM9
      cb7Q6NPQr9D54AdWk9eusGsEMiFH/MqEOK6PGA==
      =jo6C
      -----END PGP MESSAGE-----

# Private deploy key. Must be GPG encrypted.
github_deploy_key: |-
    -----BEGIN PGP MESSAGE-----
    Version: GnuPG v1

    hQEMA9aTfmR7xthMAQgAxBrdhCGZRQ7iP43AAA30NkpxX89rfca+qKSXCchnoJH1
    GqQE9Qo3hd0AdklyPdJibaN7HCJL8K9LPcjQfhx7adQHImNS2zMbS2zC+n6YfAYA
    sTjKRQENf50f9c6Zgr9R1Dhji013lA9AIXKjCTfrC/De6+e+2x1WVN0DUURICuWQ
    TciPl8ET0Did1D5p6Hi7EhUXVtfkpm66GxM87Dl3uf29IAtshAc8GnVv8/6Jz4OV
    2GfJUHcWTxAlIr1mnNobLXwDQe4/urZ9Mwzeqe3TSEd4r18efUewt1ZdyGwizrgd
    nRAx884AVDTXaVjzRFdfyW5x/hiUG66iF5jAx2icfdLrAVYl4j4+8G4BCb/1stUT
    78ADRt6VLLX4fsC4sv8TaIMRHvzclmltKmcRK26dJIrZUjS5a5zpfUniCQQNz7e5
    f6+qL5eGDb1Q/XxNN3CMQ3uG5SvvO21xcnmcfe+HR6BVLrQRVkCyH/1iVuHbbtFm
    ucWiiKfe/LAIDuSDt44LVniF0qk1wdjMzjOvN11EQwXQ1n541LzQoM/W5aXr90OA
    9HDOnLa73pEBl4czz/iyuLktEQ8lu0GmN4YaDiXBp7h9I7cZ+QVoa5LPl0oXsrnV
    RzpQ8r/Q64HO2e5IRIJnde2mMLfHetXyiVqPC3C9adonRGb84tcfy+AArfb0AINt
    LjY3bQNgDTRYWPEcqgFA8xbyzToBGi9S487zl1VMqYtR55Q/jH/ayn9lBf5I3xyp
    4GPfEcQ3erKyT5foOdUEKHoyv+3fmfD8xaYNn8piKASEUo1NuwxK2NYhbFQonmTz
    oozLW0o7ZbJxjKMpJ2rPQNnUzdN2jkdENPFgpD4xzq9b56gUh/V3u5ATkdC19CJU
    KXjG3DcRvELnecpWdspAa1f9W278/4rOVKbqGeFTG7LUqddg+Berf8/7OFgvq+xa
    MW74BUe92nRDViymTZ5r+h0zx4ooojNabq8zvQ6RyYtJ2FBZmeIU92ROIKpU/NFf
    Jk2pjfO10VAO5sZN71FA27rbPqCEptEj01nGy+HpUBj4NuQfHh7GJOvJA/cIG82Q
    dYExEhtOjLjIHyrjULS67iumrwre89m+kOfDcJ1aVs+SquOqWEx95tliNHXruRGt
    JN4p2NRnUKz13XmHPwFASa7lW0kFMgTx0/yrXLOP7jaVM1gjj3qeymHLlcA/Nnni
    VKZWucIcMW5yt94CRUWBEhgdoLLKOq52r10OCy4miXfqizBI+bNg7UtAlPPBcT7o
    JJpEWwoQzCBuo/9pvWCKWp/eVLgbk7t8wzqbi3w+jEoCAIdCI/2cN5k14+26OKPz
    GmKGHfiMJYKjnNOakgjTd9BE94SdMD2TKhnbSH7/gRKipDYAVdvUzbZQAK8vTwua
    5cQvZWEQcyNY7jKNllxFXp+K6huVVD2oMQ5uB0Llbk/Iep8YfxvVmpaiv8gaWVmN
    cZOhI2Bncltcf/n6E4h/AChd48l8ik4gad27z4SpKvvnQzA52ezKAkmKq09Qm486
    zMojQmosZ1JGyaI1c94hLXYtOT0mqTQpjOTwIwRioDJu75aRe+TsMySNeAHm6Vmc
    XizWkatFIGgxXTYhpEKPbiaRfkUAPIYUwd64yFn+BWgwL+z+uzrsPi5vVJnh+Ib9
    eKWB0qTNSb/0dE8JZdUj24QMx0EkGGwSsi8KjGGiNNBkw/BEI9q5pbXjyPc0cqDc
    ZXReGwBYQaNN0xCqNH129lJOHOlr5IUYXydIMS36FVfS8LJSvuNWni5Skr/rLe6a
    8BnMSiL2qUzzrwzwUJJ/X1L+AXEQjGX5Tuj6arZ4UCHExCL3nYQMgCHRon5egXdh
    koF4WCQgHtIiaCjkPHG17oji1rWtV5m6dldlRCO2H487ADd9WpU9DdEg4faTnB1u
    3JwDBqG97sK7PQQEq9EqlW9sCi9SfgiZC5p8arrLNIWorblGgbnbB0i2zEg7KP0W
    aihEh5xRvrOybbo0OVpzfOGY1hcYHRMDebJS2hI3A195abgzcRYAivDY0ubpeR7A
    SZGI/wdhhyUXLNbPlvSrI/xOqs5sk3HvIsCwO7ZOjnh72pay5wvI8oMBKpsHl9xU
    DCmJu3TRcQq429veL487tnG326g7OChyvD9tvjJ/zwJx5nWQZaEsSYO1qv2Xd55Z
    /M6Q4a02OReVsNvcU06U5DI9OIhnL+iuMaMtYmUHo2yLS5B5dQvtQ7111neizObN
    RCammpMhE0ToticIZINctxyO/GSd10yvaiYPjqDumAEIBcisjDCa1U8GeJf+isk9
    F/qBgw1Wbb/8mtx2UJV36y3ggn2xyisoIiJ4rOGudaMwma0fiLKkizhnG9w9bUMX
    Jn6ciH/7IuXkELYHNdCQn4XEWtKGSxkIXSY965xtxO8Y+itCjtXQO2tEx/ZpsdYK
    PysG4osdp4S4lBbSXirxWCGSdAH36f4J3rFOLqa7NB2+ioh6ZOfe0QJIrGVyJGsy
    JjrzdEmabWgcJQvaJy/eORJ+LIemQh7ZzBYOpmeGGO6pZqVjo6thzG/NWl+WgfZK
    6QL96YStvhl3uriFIdGH2XEUdrPO7c3/Wy5L21EMZJACi0dJQm2l7dn76Lv8f853
    NfHtV/tMPDAq6nyMQmJTLML8mwxe0WEOHn45NbGy3smwFIToYW9P3sZIsiQCmvET
    MvjB+ZabfmeyRQ+h33gvm3uWfCqkatpT+O3sx95DzZnyuv+zPRTD8dlwvvKqyeg6
    bywIGP7fXrm65Dx3B5yfhXbrei20h0Ye+qGnbm5lPXwNsEJU4YQocJOCSbRQdfnY
    iqI0sf6ExhZ9kX2uejhBoscqls7gFVX5ti8PokVoUpkAZl30LavrFrB7KC+dzD6u
    ZrdKeBl5re9eWUHDE3g/04B9/8dF7z/btrxLwxAN2nbZfR/e0gll+/YX0SbTLUwU
    Ohp3dBLuL/nBoXO1CUFQq4VPqOlMDiFl/atzBvcl7HRVUvw5gRDJG0ZAxIDVEf79
    J8KDjRMJMiTZg5nrxoFNJQPTXTXKZ0wezq1CHbmX+NUaZz2jyZWAB04RFlfQIPjh
    gqOXBSMY0cV1XgBk6P9P/GXBNWmsAKtTXngqfsn8i+9c+MXzjkY1CG61ZWipFfm+
    ZVMhhna+bLPfpKJelUYP3EoykBgo1o7DB0vRmODaMToQc4cp975jgUwI5x3tS3PF
    +Ot54KOyX4TB/XVF7Uw86mokKcbsZdgqwjVuv+7zxc6ruHWFiNzp7O58P6L9DgkL
    g74/m/JcU8pjDB/d/rtz6aJqYUy0jkkhrcHZQXq2oeX0j0M9UsE/HgOLXR+kzUjR
    WPs2S7jNybQyudWzyycz3EUNqmUyuxs6vArT1ia6c6dcVXtQm5ZxuzTDKnFlTLpl
    2Ns79lptAcZVWxJDoWFCGkv2NIhm/6UPvQwJfDHBdwWTqzN9UGXB8YFACegrv+qp
    7re8cAast9Ws5/Dh3tH9zEImMO86GZOL3dPbfPXByfJVrFOEmQkesjhAyTQw/E6R
    29YWcms+blU1QX7wazDKewIWLuZUDChkmtNAh6uYvZuJywy39wKcmXtU/DYTit/w
    C5sj7qVvUc3WpKi6dI3LTqmbx+XR1nfoZe0FPChccZtGG0kHrADxuGH3Ovmd2i7E
    PvKtzIPGNOKciI5KGPgjOEpAtm4ou51N7C0vj6MeqTB/XITwSgPAesxzsg+bBoxb
    trN0/fpfiRoAQoWw9nD5WOXcQiYc5JTUc5K5Bo3KfMmbyWMMBj4drQ==
    =rJBX
    -----END PGP MESSAGE-----


# Uncomment and update ssl_key and ssl_cert to enabled signed SSL/
# Must be GPG encrypted.
#{% if 'balancer' in grains['roles'] %}
ssl_key: |-
    -----BEGIN PGP MESSAGE-----
    Version: GnuPG v1

    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
    =Egu4
    -----END PGP MESSAGE-----
ssl_cert: |-
    -----BEGIN PGP MESSAGE-----
    Version: GnuPG v1

    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
    qcw3eM9FJ3/JPFhfmhuSTm9+UJ+vJow=
    =zp2f
    -----END PGP MESSAGE-----

#{% endif %}